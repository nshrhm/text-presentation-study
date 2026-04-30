#!/usr/bin/env python3
"""
Data Visualization Program for Academic Research
Creates high-quality violin plots, box plots, and strip plots for A/B group comparison
"""

import argparse
import os
import sys
import tempfile
from pathlib import Path

cache_dir = Path(tempfile.gettempdir()) / 'text_presentation_study_cache'
cache_dir.mkdir(parents=True, exist_ok=True)
matplotlib_cache_dir = cache_dir / 'matplotlib'
xdg_cache_dir = cache_dir / 'xdg'
matplotlib_cache_dir.mkdir(parents=True, exist_ok=True)
xdg_cache_dir.mkdir(parents=True, exist_ok=True)
os.environ.setdefault('MPLCONFIGDIR', str(matplotlib_cache_dir))
os.environ.setdefault('XDG_CACHE_HOME', str(xdg_cache_dir))

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from study_analysis import (
    GROUP_LABELS,
    MEASURE_LABELS,
    SUBJECTIVE_MEASURES,
    load_dataset,
)

# Set style for academic publication
plt.style.use('default')
sns.set_palette("Set2")

def setup_matplotlib():
    """Configure matplotlib for academic publication quality"""
    plt.rcParams['figure.dpi'] = 300
    plt.rcParams['savefig.dpi'] = 300
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['xtick.labelsize'] = 12
    plt.rcParams['ytick.labelsize'] = 12
    plt.rcParams['legend.fontsize'] = 12
    plt.rcParams['figure.titlesize'] = 18
    plt.rcParams['font.family'] = ['DejaVu Sans', 'sans-serif']

def get_labels():
    """Return English labels for reviewer-facing figures."""
    return {
        **MEASURE_LABELS,
        'group_a': GROUP_LABELS['A'],
        'group_b': GROUP_LABELS['B'],
        'value': 'Value',
        'title_subjective': 'Comparison of Subjective Evaluation Items',
        'title_time': 'Comparison of Reading Time'
    }

def create_horizontal_plot(data, columns, labels, output_dir, filename_stem, title):
    """Create horizontal violin plot with box plot and strip plot overlay"""
    n_cols = len(columns)
    fig, axes = plt.subplots(n_cols, 1, figsize=(10, 2.5 * n_cols))
    
    if n_cols == 1:
        axes = [axes]
    
    colors = ['lightblue', 'lightcoral']
    
    for i, col in enumerate(columns):
        ax = axes[i]
        
        # Create violin plot (horizontal, no fill)
        violin_parts = ax.violinplot([data[data['group'] == 'A'][col].values,
                                     data[data['group'] == 'B'][col].values],
                                   positions=[0, 1], vert=False, showmeans=False,
                                   showmedians=False, showextrema=False)
        
        # Style violin plots (no fill)
        for j, pc in enumerate(violin_parts['bodies']):
            pc.set_facecolor('none')
            pc.set_edgecolor(colors[j])
            pc.set_linewidth(1.5)
            pc.set_alpha(0.8)
        
        # Create box plots (horizontal, no fill)
        box_data = [data[data['group'] == 'A'][col].values,
                   data[data['group'] == 'B'][col].values]
        
        bp = ax.boxplot(box_data, positions=[0, 1], vert=False, patch_artist=True,
                       widths=0.3, showfliers=False)
        
        # Style box plots (no fill)
        for j, box in enumerate(bp['boxes']):
            box.set_facecolor('none')
            box.set_edgecolor(colors[j])
            box.set_linewidth(2)
        
        for element in ['whiskers', 'caps', 'medians']:
            for j, line in enumerate(bp[element]):
                line.set_color(colors[j//2] if element in ['whiskers', 'caps'] else 'black')
                line.set_linewidth(2 if element == 'medians' else 1.5)
        
        # Add strip plot (jittered points)
        rng = np.random.default_rng(42 + i)
        for j, group in enumerate(['A', 'B']):
            group_data = data[data['group'] == group][col].values
            y_pos = j + rng.normal(0, 0.05, len(group_data))
            ax.scatter(group_data, y_pos, alpha=0.6, s=30, color=colors[j], 
                      edgecolor='white', linewidth=0.5, zorder=3)
        
        # Customize axes
        ax.set_yticks([0, 1])
        ax.set_yticklabels([labels['group_a'], labels['group_b']])
        ax.set_xlabel(labels[col] if col != 'time' else labels['time'])
        ax.grid(True, alpha=0.3, axis='x')
        ax.set_axisbelow(True)
        
        # Set y-axis limits
        ax.set_ylim(-0.5, 1.5)
        
        # Add statistical information as text
        mean_a = data[data['group'] == 'A'][col].mean()
        mean_b = data[data['group'] == 'B'][col].mean()
        std_a = data[data['group'] == 'A'][col].std()
        std_b = data[data['group'] == 'B'][col].std()
        stats_text = (
            f'Group A: mean={mean_a:.1f}, SD={std_a:.1f}\n'
            f'Group B: mean={mean_b:.1f}, SD={std_b:.1f}'
        )
        
        ax.text(0.98, 0.02, stats_text, transform=ax.transAxes, 
                fontsize=10, verticalalignment='bottom', horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.suptitle(title, fontsize=16, y=0.98)
    plt.tight_layout()
    
    # Save in both formats
    output_dir.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_dir / f'{filename_stem}.png', dpi=300, bbox_inches='tight')
    plt.savefig(output_dir / f'{filename_stem}.pdf', bbox_inches='tight')
    plt.close()

def main():
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description='Create academic quality data visualizations')
    parser.add_argument('--data', type=Path, default=Path(__file__).with_name('data_all.csv'),
                        help='Path to the CSV dataset')
    parser.add_argument('--output-dir', type=Path, default=repo_root / 'paper' / 'images',
                        help='Directory for generated figure files')
    args = parser.parse_args()
    
    print("Starting visualization")
    
    # Setup
    setup_matplotlib()
    labels = get_labels()
    
    # Load data
    try:
        data = load_dataset(args.data)
        print(f"Successfully loaded data with {len(data)} rows")
    except FileNotFoundError:
        print(f"Error: dataset not found: {args.data}")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)
    
    print(f"Groups: {data['group'].unique()}")
    print(f"Columns: {data.columns.tolist()}")
    
    try:
        # Create Graph 1: Subjective evaluation items
        print("Creating Graph 1: Subjective evaluation items...")
        create_horizontal_plot(data, SUBJECTIVE_MEASURES, labels, args.output_dir,
                              'subjective_en', labels['title_subjective'])
        print("Graph 1 completed successfully")
        
        # Create Graph 2: Time comparison
        print("Creating Graph 2: Time comparison...")
        time_columns = ['time']
        create_horizontal_plot(data, time_columns, labels, args.output_dir,
                              'time_en', labels['title_time'])
        print("Graph 2 completed successfully")
        
        print(f"All graphs saved successfully to {args.output_dir}:")
        print("- subjective_en.png/pdf")
        print("- time_en.png/pdf")
        
    except Exception as e:
        print(f"Error creating graphs: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
