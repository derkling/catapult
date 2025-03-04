# Copyright (c) 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'tracing_css_files': [
      'tracing/ui/base/line_chart.css',
      'tracing/ui/base/list_view.css',
      'tracing/ui/base/pie_chart.css',
      'tracing/ui/extras/about_tracing/common.css',
      'tracing/ui/extras/chrome/cc/display_item_list_view.css',
      'tracing/ui/extras/chrome/cc/layer_picker.css',
      'tracing/ui/extras/chrome/cc/layer_tree_host_impl_view.css',
      'tracing/ui/extras/chrome/cc/layer_view.css',
      'tracing/ui/extras/chrome/cc/picture_ops_chart_summary_view.css',
      'tracing/ui/extras/chrome/cc/picture_ops_chart_view.css',
      'tracing/ui/extras/chrome/cc/picture_ops_list_view.css',
      'tracing/ui/extras/chrome/cc/picture_view.css',
      'tracing/ui/extras/chrome/gpu/state_view.css',
      'tracing/ui/extras/system_stats/system_stats_instance_track.css',
      'tracing/ui/extras/system_stats/system_stats_snapshot_view.css',
      'tracing/ui/tracks/drawing_container.css',
      'tracing/ui/tracks/object_instance_track.css',
      'tracing/ui/tracks/process_track_base.css',
      'tracing/ui/tracks/rect_track.css',
      'tracing/ui/tracks/ruler_track.css',
      'tracing/ui/tracks/spacing_track.css',
      'tracing/ui/tracks/thread_track.css',
      'tracing/ui/tracks/track.css',
    ],
    'tracing_js_html_files': [
      'tracing/base/base.html',
      'tracing/base/base64.html',
      'tracing/base/bbox2.html',
      'tracing/base/category_util.html',
      'tracing/base/color.html',
      'tracing/base/color_scheme.html',
      'tracing/base/event.html',
      'tracing/base/event_target.html',
      'tracing/base/extension_registry.html',
      'tracing/base/extension_registry_base.html',
      'tracing/base/extension_registry_basic.html',
      'tracing/base/extension_registry_type_based.html',
      'tracing/base/guid.html',
      'tracing/base/interval_tree.html',
      'tracing/base/iteration_helpers.html',
      'tracing/base/math.html',
      'tracing/base/multi_dimensional_view.html',
      'tracing/base/quad.html',
      'tracing/base/raf.html',
      'tracing/base/range.html',
      'tracing/base/range_utils.html',
      'tracing/base/rect.html',
      'tracing/base/settings.html',
      'tracing/base/sorted_array_utils.html',
      'tracing/base/statistics.html',
      'tracing/base/task.html',
      'tracing/base/timing.html',
      'tracing/base/units/generic_table.html',
      'tracing/base/units/histogram.html',
      'tracing/base/units/scalar.html',
      'tracing/base/units/time_display_mode.html',
      'tracing/base/units/unit.html',
      'tracing/base/utils.html',
      'tracing/core/auditor.html',
      'tracing/core/filter.html',
      'tracing/core/scripting_controller.html',
      'tracing/core/scripting_object.html',
      'tracing/extras/android/android_app.html',
      'tracing/extras/android/android_auditor.html',
      'tracing/extras/android/android_surface_flinger.html',
      'tracing/extras/chrome/cc/cc.html',
      'tracing/extras/chrome/cc/constants.html',
      'tracing/extras/chrome/cc/debug_colors.html',
      'tracing/extras/chrome/cc/display_item_list.html',
      'tracing/extras/chrome/cc/input_latency_async_slice.html',
      'tracing/extras/chrome/cc/layer_impl.html',
      'tracing/extras/chrome/cc/layer_tree_host_impl.html',
      'tracing/extras/chrome/cc/layer_tree_impl.html',
      'tracing/extras/chrome/cc/picture.html',
      'tracing/extras/chrome/cc/picture_as_image_data.html',
      'tracing/extras/chrome/cc/raster_task.html',
      'tracing/extras/chrome/cc/region.html',
      'tracing/extras/chrome/cc/render_pass.html',
      'tracing/extras/chrome/cc/tile.html',
      'tracing/extras/chrome/cc/tile_coverage_rect.html',
      'tracing/extras/chrome/cc/util.html',
      'tracing/extras/chrome/chrome_auditor.html',
      'tracing/extras/chrome/chrome_user_friendly_category_driver.html',
      'tracing/extras/chrome/gpu/gpu_async_slice.html',
      'tracing/extras/chrome/gpu/state.html',
      'tracing/extras/chrome/layout_object.html',
      'tracing/extras/chrome_config.html',
      'tracing/extras/importer/android/event_log_importer.html',
      'tracing/extras/importer/battor_importer.html',
      'tracing/extras/importer/ddms_importer.html',
      'tracing/extras/importer/etw/etw_importer.html',
      'tracing/extras/importer/etw/eventtrace_parser.html',
      'tracing/extras/importer/etw/parser.html',
      'tracing/extras/importer/etw/process_parser.html',
      'tracing/extras/importer/etw/thread_parser.html',
      'tracing/extras/importer/gcloud_trace/gcloud_trace_importer.html',
      'tracing/extras/importer/gzip_importer.html',
      'tracing/extras/importer/jszip.html',
      'tracing/extras/importer/linux_perf/android_parser.html',
      'tracing/extras/importer/linux_perf/binder_parser.html',
      'tracing/extras/importer/linux_perf/bus_parser.html',
      'tracing/extras/importer/linux_perf/clock_parser.html',
      'tracing/extras/importer/linux_perf/cpufreq_parser.html',
      'tracing/extras/importer/linux_perf/disk_parser.html',
      'tracing/extras/importer/linux_perf/drm_parser.html',
      'tracing/extras/importer/linux_perf/exynos_parser.html',
      'tracing/extras/importer/linux_perf/ftrace_importer.html',
      'tracing/extras/importer/linux_perf/gesture_parser.html',
      'tracing/extras/importer/linux_perf/i915_parser.html',
      'tracing/extras/importer/linux_perf/irq_parser.html',
      'tracing/extras/importer/linux_perf/kfunc_parser.html',
      'tracing/extras/importer/linux_perf/mali_parser.html',
      'tracing/extras/importer/linux_perf/memreclaim_parser.html',
      'tracing/extras/importer/linux_perf/parser.html',
      'tracing/extras/importer/linux_perf/power_parser.html',
      'tracing/extras/importer/linux_perf/regulator_parser.html',
      'tracing/extras/importer/linux_perf/sched_parser.html',
      'tracing/extras/importer/linux_perf/sync_parser.html',
      'tracing/extras/importer/linux_perf/workqueue_parser.html',
      'tracing/extras/importer/trace2html_importer.html',
      'tracing/extras/importer/trace_code_entry.html',
      'tracing/extras/importer/trace_code_map.html',
      'tracing/extras/importer/trace_event_importer.html',
      'tracing/extras/importer/v8/codemap.html',
      'tracing/extras/importer/v8/log_reader.html',
      'tracing/extras/importer/v8/splaytree.html',
      'tracing/extras/importer/v8/v8_log_importer.html',
      'tracing/extras/importer/zip_importer.html',
      'tracing/extras/lean_config.html',
      'tracing/extras/measure/measure.html',
      'tracing/extras/measure/measure_async_slice.html',
      'tracing/extras/net/net.html',
      'tracing/extras/net/net_async_slice.html',
      'tracing/extras/rail/proto_ir.html',
      'tracing/extras/system_stats/system_stats_snapshot.html',
      'tracing/extras/systrace_config.html',
      'tracing/extras/tquery/context.html',
      'tracing/extras/tquery/filter.html',
      'tracing/extras/tquery/filter_all_of.html',
      'tracing/extras/tquery/filter_any_of.html',
      'tracing/extras/tquery/filter_has_ancestor.html',
      'tracing/extras/tquery/filter_has_duration.html',
      'tracing/extras/tquery/filter_has_title.html',
      'tracing/extras/tquery/filter_is_top_level.html',
      'tracing/extras/tquery/tquery.html',
      'tracing/extras/vsync/vsync_auditor.html',
      'tracing/importer/empty_importer.html',
      'tracing/importer/find_input_expectations.html',
      'tracing/importer/import.html',
      'tracing/importer/importer.html',
      'tracing/importer/simple_line_reader.html',
      'tracing/importer/user_model_builder.html',
      'tracing/metrics/system_health/animation_smoothness_metric.html',
      'tracing/metrics/system_health/animation_throughput_metric.html',
      'tracing/metrics/system_health/efficiency_metric.html',
      'tracing/metrics/system_health/responsiveness_metric.html',
      'tracing/metrics/system_health/system_health_metric.html',
      'tracing/metrics/system_health/utils.html',
      'tracing/metrics/ui/system_health/system_health_side_panel.html',
      'tracing/metrics/ui/system_health/system_health_span.html',
      'tracing/model/activity.html',
      'tracing/model/alert.html',
      'tracing/model/annotation.html',
      'tracing/model/async_slice.html',
      'tracing/model/async_slice_group.html',
      'tracing/model/attribute.html',
      'tracing/model/comment_box_annotation.html',
      'tracing/model/compound_event_selection_state.html',
      'tracing/model/constants.html',
      'tracing/model/container_memory_dump.html',
      'tracing/model/counter.html',
      'tracing/model/counter_sample.html',
      'tracing/model/counter_series.html',
      'tracing/model/cpu.html',
      'tracing/model/cpu_slice.html',
      'tracing/model/device.html',
      'tracing/model/event.html',
      'tracing/model/event_container.html',
      'tracing/model/event_info.html',
      'tracing/model/event_registry.html',
      'tracing/model/event_set.html',
      'tracing/model/flow_event.html',
      'tracing/model/frame.html',
      'tracing/model/global_memory_dump.html',
      'tracing/model/heap_dump.html',
      'tracing/model/helpers/android_model_helper.html',
      'tracing/model/helpers/chrome_browser_helper.html',
      'tracing/model/helpers/chrome_gpu_helper.html',
      'tracing/model/helpers/chrome_model_helper.html',
      'tracing/model/helpers/chrome_process_helper.html',
      'tracing/model/helpers/chrome_renderer_helper.html',
      'tracing/model/instant_event.html',
      'tracing/model/ir_coverage.html',
      'tracing/model/kernel.html',
      'tracing/model/location.html',
      'tracing/model/memory_allocator_dump.html',
      'tracing/model/model.html',
      'tracing/model/model_indices.html',
      'tracing/model/model_settings.html',
      'tracing/model/model_stats.html',
      'tracing/model/object_collection.html',
      'tracing/model/object_instance.html',
      'tracing/model/object_snapshot.html',
      'tracing/model/power_sample.html',
      'tracing/model/power_series.html',
      'tracing/model/process.html',
      'tracing/model/process_base.html',
      'tracing/model/process_memory_dump.html',
      'tracing/model/proxy_selectable_item.html',
      'tracing/model/rect_annotation.html',
      'tracing/model/sample.html',
      'tracing/model/scoped_id.html',
      'tracing/model/selectable_item.html',
      'tracing/model/selection_state.html',
      'tracing/model/slice.html',
      'tracing/model/slice_group.html',
      'tracing/model/source_info/js_source_info.html',
      'tracing/model/source_info/source_info.html',
      'tracing/model/stack_frame.html',
      'tracing/model/thread.html',
      'tracing/model/thread_slice.html',
      'tracing/model/thread_time_slice.html',
      'tracing/model/time_to_object_instance_map.html',
      'tracing/model/timed_event.html',
      'tracing/model/user_model/animation_expectation.html',
      'tracing/model/user_model/idle_expectation.html',
      'tracing/model/user_model/load_expectation.html',
      'tracing/model/user_model/response_expectation.html',
      'tracing/model/user_model/user_expectation.html',
      'tracing/model/x_marker_annotation.html',
      'tracing/ui/analysis/alert_sub_view.html',
      'tracing/ui/analysis/analysis_link.html',
      'tracing/ui/analysis/analysis_sub_view.html',
      'tracing/ui/analysis/analysis_view.html',
      'tracing/ui/analysis/container_memory_dump_sub_view.html',
      'tracing/ui/analysis/counter_sample_sub_view.html',
      'tracing/ui/analysis/flow_classifier.html',
      'tracing/ui/analysis/frame_power_usage_chart.html',
      'tracing/ui/analysis/generic_object_view.html',
      'tracing/ui/analysis/memory_dump_allocator_details_pane.html',
      'tracing/ui/analysis/memory_dump_header_pane.html',
      'tracing/ui/analysis/memory_dump_heap_details_pane.html',
      'tracing/ui/analysis/memory_dump_overview_pane.html',
      'tracing/ui/analysis/memory_dump_sub_view_util.html',
      'tracing/ui/analysis/memory_dump_vm_regions_details_pane.html',
      'tracing/ui/analysis/multi_async_slice_sub_view.html',
      'tracing/ui/analysis/multi_cpu_slice_sub_view.html',
      'tracing/ui/analysis/multi_event_details_table.html',
      'tracing/ui/analysis/multi_event_sub_view.html',
      'tracing/ui/analysis/multi_event_summary.html',
      'tracing/ui/analysis/multi_event_summary_table.html',
      'tracing/ui/analysis/multi_flow_event_sub_view.html',
      'tracing/ui/analysis/multi_frame_sub_view.html',
      'tracing/ui/analysis/multi_instant_event_sub_view.html',
      'tracing/ui/analysis/multi_object_sub_view.html',
      'tracing/ui/analysis/multi_power_sample_sub_view.html',
      'tracing/ui/analysis/multi_sample_sub_view.html',
      'tracing/ui/analysis/multi_thread_slice_sub_view.html',
      'tracing/ui/analysis/multi_thread_time_slice_sub_view.html',
      'tracing/ui/analysis/multi_user_expectation_sub_view.html',
      'tracing/ui/analysis/object_instance_view.html',
      'tracing/ui/analysis/object_snapshot_view.html',
      'tracing/ui/analysis/power_sample_summary_table.html',
      'tracing/ui/analysis/power_sample_table.html',
      'tracing/ui/analysis/related_events.html',
      'tracing/ui/analysis/selection_summary_table.html',
      'tracing/ui/analysis/single_async_slice_sub_view.html',
      'tracing/ui/analysis/single_cpu_slice_sub_view.html',
      'tracing/ui/analysis/single_event_sub_view.html',
      'tracing/ui/analysis/single_flow_event_sub_view.html',
      'tracing/ui/analysis/single_frame_sub_view.html',
      'tracing/ui/analysis/single_instant_event_sub_view.html',
      'tracing/ui/analysis/single_object_instance_sub_view.html',
      'tracing/ui/analysis/single_object_snapshot_sub_view.html',
      'tracing/ui/analysis/single_power_sample_sub_view.html',
      'tracing/ui/analysis/single_sample_sub_view.html',
      'tracing/ui/analysis/single_thread_slice_sub_view.html',
      'tracing/ui/analysis/single_thread_time_slice_sub_view.html',
      'tracing/ui/analysis/single_user_expectation_sub_view.html',
      'tracing/ui/analysis/stack_frame.html',
      'tracing/ui/analysis/stacked_pane.html',
      'tracing/ui/analysis/stacked_pane_view.html',
      'tracing/ui/analysis/tab_view.html',
      'tracing/ui/annotations/annotation_view.html',
      'tracing/ui/annotations/comment_box_annotation_view.html',
      'tracing/ui/annotations/rect_annotation_view.html',
      'tracing/ui/annotations/x_marker_annotation_view.html',
      'tracing/ui/base/animation.html',
      'tracing/ui/base/animation_controller.html',
      'tracing/ui/base/camera.html',
      'tracing/ui/base/chart_base.html',
      'tracing/ui/base/chart_base_2d.html',
      'tracing/ui/base/chart_base_2d_brushable_x.html',
      'tracing/ui/base/color_legend.html',
      'tracing/ui/base/constants.html',
      'tracing/ui/base/container_that_decorates_its_children.html',
      'tracing/ui/base/d3.html',
      'tracing/ui/base/deep_utils.html',
      'tracing/ui/base/dom_helpers.html',
      'tracing/ui/base/drag_handle.html',
      'tracing/ui/base/draw_helpers.html',
      'tracing/ui/base/dropdown.html',
      'tracing/ui/base/elided_cache.html',
      'tracing/ui/base/event_presenter.html',
      'tracing/ui/base/fast_rect_renderer.html',
      'tracing/ui/base/favicons.html',
      'tracing/ui/base/grouping_table.html',
      'tracing/ui/base/grouping_table_groupby_picker.html',
      'tracing/ui/base/heading.html',
      'tracing/ui/base/hot_key.html',
      'tracing/ui/base/hotkey_controller.html',
      'tracing/ui/base/info_bar.html',
      'tracing/ui/base/info_bar_group.html',
      'tracing/ui/base/line_chart.html',
      'tracing/ui/base/list_view.html',
      'tracing/ui/base/mouse_mode_icon.html',
      'tracing/ui/base/mouse_mode_selector.html',
      'tracing/ui/base/mouse_modes.html',
      'tracing/ui/base/mouse_tracker.html',
      'tracing/ui/base/overlay.html',
      'tracing/ui/base/pie_chart.html',
      'tracing/ui/base/polymer_utils.html',
      'tracing/ui/base/quad_stack_view.html',
      'tracing/ui/base/table.html',
      'tracing/ui/base/timing_tool.html',
      'tracing/ui/base/toolbar_button.html',
      'tracing/ui/base/ui.html',
      'tracing/ui/base/ui_state.html',
      'tracing/ui/base/utils.html',
      'tracing/ui/brushing_state.html',
      'tracing/ui/brushing_state_controller.html',
      'tracing/ui/extras/about_tracing/about_tracing.html',
      'tracing/ui/extras/about_tracing/inspector_connection.html',
      'tracing/ui/extras/about_tracing/inspector_tracing_controller_client.html',
      'tracing/ui/extras/about_tracing/profiling_view.html',
      'tracing/ui/extras/about_tracing/record_controller.html',
      'tracing/ui/extras/about_tracing/record_selection_dialog.html',
      'tracing/ui/extras/about_tracing/tracing_controller_client.html',
      'tracing/ui/extras/about_tracing/xhr_based_tracing_controller_client.html',
      'tracing/ui/extras/chrome/cc/cc.html',
      'tracing/ui/extras/chrome/cc/display_item_debugger.html',
      'tracing/ui/extras/chrome/cc/display_item_list_view.html',
      'tracing/ui/extras/chrome/cc/layer_picker.html',
      'tracing/ui/extras/chrome/cc/layer_tree_host_impl_view.html',
      'tracing/ui/extras/chrome/cc/layer_tree_quad_stack_view.html',
      'tracing/ui/extras/chrome/cc/layer_view.html',
      'tracing/ui/extras/chrome/cc/picture_debugger.html',
      'tracing/ui/extras/chrome/cc/picture_ops_chart_summary_view.html',
      'tracing/ui/extras/chrome/cc/picture_ops_chart_view.html',
      'tracing/ui/extras/chrome/cc/picture_ops_list_view.html',
      'tracing/ui/extras/chrome/cc/picture_view.html',
      'tracing/ui/extras/chrome/cc/raster_task_selection.html',
      'tracing/ui/extras/chrome/cc/raster_task_view.html',
      'tracing/ui/extras/chrome/cc/selection.html',
      'tracing/ui/extras/chrome/cc/tile_view.html',
      'tracing/ui/extras/chrome/gpu/gpu.html',
      'tracing/ui/extras/chrome/gpu/state_view.html',
      'tracing/ui/extras/chrome_config.html',
      'tracing/ui/extras/full_config.html',
      'tracing/ui/extras/highlighter/vsync_highlighter.html',
      'tracing/ui/extras/lean_config.html',
      'tracing/ui/extras/side_panel/alerts_side_panel.html',
      'tracing/ui/extras/side_panel/input_latency_side_panel.html',
      'tracing/ui/extras/side_panel/time_summary_side_panel.html',
      'tracing/ui/extras/system_stats/system_stats.html',
      'tracing/ui/extras/system_stats/system_stats_instance_track.html',
      'tracing/ui/extras/system_stats/system_stats_snapshot_view.html',
      'tracing/ui/extras/systrace_config.html',
      'tracing/ui/find_control.html',
      'tracing/ui/find_controller.html',
      'tracing/ui/scripting_control.html',
      'tracing/ui/side_panel/file_size_stats_side_panel.html',
      'tracing/ui/side_panel/side_panel.html',
      'tracing/ui/side_panel/side_panel_container.html',
      'tracing/ui/timeline_display_transform.html',
      'tracing/ui/timeline_display_transform_animations.html',
      'tracing/ui/timeline_interest_range.html',
      'tracing/ui/timeline_track_view.html',
      'tracing/ui/timeline_view.html',
      'tracing/ui/timeline_view_help_overlay.html',
      'tracing/ui/timeline_view_metadata_overlay.html',
      'tracing/ui/timeline_viewport.html',
      'tracing/ui/tracks/alert_track.html',
      'tracing/ui/tracks/async_slice_group_track.html',
      'tracing/ui/tracks/chart_axis.html',
      'tracing/ui/tracks/chart_point.html',
      'tracing/ui/tracks/chart_series.html',
      'tracing/ui/tracks/chart_track.html',
      'tracing/ui/tracks/chart_transform.html',
      'tracing/ui/tracks/container_to_track_map.html',
      'tracing/ui/tracks/container_track.html',
      'tracing/ui/tracks/counter_track.html',
      'tracing/ui/tracks/cpu_track.html',
      'tracing/ui/tracks/device_track.html',
      'tracing/ui/tracks/drawing_container.html',
      'tracing/ui/tracks/event_to_track_map.html',
      'tracing/ui/tracks/frame_track.html',
      'tracing/ui/tracks/global_memory_dump_track.html',
      'tracing/ui/tracks/highlighter.html',
      'tracing/ui/tracks/interaction_track.html',
      'tracing/ui/tracks/kernel_track.html',
      'tracing/ui/tracks/letter_dot_track.html',
      'tracing/ui/tracks/memory_dump_track_util.html',
      'tracing/ui/tracks/model_track.html',
      'tracing/ui/tracks/multi_row_track.html',
      'tracing/ui/tracks/object_instance_group_track.html',
      'tracing/ui/tracks/object_instance_track.html',
      'tracing/ui/tracks/power_series_track.html',
      'tracing/ui/tracks/process_memory_dump_track.html',
      'tracing/ui/tracks/process_summary_track.html',
      'tracing/ui/tracks/process_track.html',
      'tracing/ui/tracks/process_track_base.html',
      'tracing/ui/tracks/rect_track.html',
      'tracing/ui/tracks/ruler_track.html',
      'tracing/ui/tracks/sample_track.html',
      'tracing/ui/tracks/slice_group_track.html',
      'tracing/ui/tracks/slice_track.html',
      'tracing/ui/tracks/spacing_track.html',
      'tracing/ui/tracks/stacked_bars_track.html',
      'tracing/ui/tracks/thread_track.html',
      'tracing/ui/tracks/track.html',
      'tracing/ui/units/array_of_numbers_span.html',
      'tracing/ui/units/generic_table_view.html',
      'tracing/ui/units/preferred_display_unit.html',
      'tracing/ui/units/scalar_span.html',
      'tracing/ui/units/time_duration_span.html',
      'tracing/ui/units/time_stamp_span.html',
      'tracing/ui/view_specific_brushing_state.html',
    ],
    'tracing_img_files': [
      'tracing/ui/extras/chrome/cc/images/input-event.png',
      'tracing/ui/extras/chrome/gpu/images/checkerboard.png',
      'tracing/ui/images/chrome-left.png',
      'tracing/ui/images/chrome-mid.png',
      'tracing/ui/images/chrome-right.png',
      'tracing/ui/images/ui-states.png',
    ],
    'tracing_files': [
      '<@(tracing_css_files)',
      '<@(tracing_js_html_files)',
      '<@(tracing_img_files)',
    ],
  }
}
